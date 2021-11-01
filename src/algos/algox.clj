(ns algos.algox
  (:require [clojure.set :as set]
            [clojure.pprint :as pprint]))

(defn exclude-rows [ex-s x y s]
  (reduce
    (fn [[x y s] ex]
      (let [new-x (set/difference x ex)
            new-y (set/difference y ex)
            new-s  (filter
                     (fn [si]
                       (empty? (set/intersection si ex))
                       )
                     s)]
        [new-x new-y new-s]
        )
      )
    [x y s]
    ex-s)
  )

(defn find-general-solutions [x y s solution solutions find-first?]
  (if (empty? x)
    (set/union solutions #{solution})
    (let [c (first x)
          candidates (filter #(% c) s)
          new-s (fn [candidate]
                  (filter
                    (fn [si]
                      (empty? (set/intersection si candidate))
                      )
                    s))]
      (if (empty? candidates)
        solutions
        (reduce
          (fn [solutions candidate]
            (let [solutions (find-general-solutions (set/difference x candidate) (set/difference y candidate)
                                    (new-s candidate) (conj solution candidate) solutions find-first?)]
              (if (and find-first? (not (empty? solutions))) (reduced solutions)
                                                             solutions)
              ))
          solutions
          candidates)
        )
      )
    )
  )

(defn general-exact-cover
  " given a collection S of subsets of a primary set X, secondary set Y, an exact cover is a subcollection S* of S such that each element in
  X is contained in exactly one subset in S* and each element in Y is contained in at most one subset in S*"
  [x y s ex-s find-first?]
  (let [[x y s] (exclude-rows ex-s x y s)]
    (loop [x x y y s s solutions #{}]
      (if (empty? x)
        solutions
        (find-general-solutions x y s #{} solutions find-first?)
        )
      )
    )
  )

(defn find-solutions [x s solution solutions]
  (if (empty? x)
    (set/union solutions #{solution})
    (let [c (first x)
          candidates (filter #(% c) s)
          new-s (fn [candidate]
                  (filter
                    (fn [si]
                      (empty? (set/intersection si candidate))
                      )
                    s))]
      (if (empty? candidates)
        solutions
        (apply set/union
               (map
                 (fn [candidate]
                   (find-solutions (set/difference x candidate)
                                   (new-s candidate) (conj solution candidate) solutions))
                 candidates))
        )
      )
    )
  )

(defn exact-cover
  " given a collection S of subsets of a set X, an exact cover is a subcollection S* of S such that each element in
  X is contained in exactly one subset in S*"
  [x s]
  (loop [x x s s solutions #{}]
    (if (empty? x)
      solutions
      (find-solutions x s #{} solutions)
      )
    )
  )

(defn exact-cover-2 [x s]
  (general-exact-cover x #{} s #{} false))

(defn queens [n]
  (let [n1 (- n 1)
        x (into #{} (range (* 2 n)))
        y (into #{} (range (* 2 n) (- (* 6 n) 6)))
        s-ij (map
            (fn [[i j]]
              (let [cols #{i (+ n j)}
                    cols (cond
                           (and (zero? i) (zero? j)) cols
                           (and (= i n1) (= j n1)) cols
                           :else (conj cols (+ (* 2 n) (dec (+ i j))))
                           )
                    cols (cond
                           (and (zero? i) (= j n1)) cols
                           (and (zero? j) (= i n1)) cols
                           :else (conj cols (+ (- (* 4 n) 3) (+ (- n 2) (- i j)) ))
                           )]
                    [cols [i j]]
                )
              )
            (for [i (range n) j (range n)] [i j]))
        s-ij-map (into {} s-ij)
        s (keys s-ij-map)
        solutions (general-exact-cover x y (into #{} s) #{} false)]
    (into #{}
          (map
      (fn [solution]
        (into #{} (map s-ij-map solution))
        )
      solutions))
    )
  )
(defn exp [x n]
  (reduce * (repeat n x)))

(defn sudoku-to-row [cell]
  (let [[[r c] k] cell
        b (+ (* 3 (quot r 3)) (quot c 3))
        col-row (+ k (* r 9)) ;row r occupied by k
        col-col (+ 81 (+ k (* c 9)))           ;col c occupied by k
        col-box (+ (* 81 2) (+ k (* 9 b)))
        col-cell (+ (* 81 3) (+ (* r 9) c))
        ]
    #{col-row col-col col-box col-cell}
    )
  )

(defn sudoku-to-cover []
  (let [cols (into #{} (range (* 9 9)))                   ;each rank occupied by 1-9
        cols (into cols (map #(+ 81 %) (range (* 9 9))))                    ;each file occupied by 1-9
        cols (into cols (map #(+ (* 81 2) %) (range (* 9 9))))                    ;each 3X3 occupied by 1-9
        cols (into cols (map #(+ (* 81 3) %) (range 81)) )            ;each cell is occupied by exactly one number
        rows (map
               sudoku-to-row
               (for [r (range 9) c (range 9) k (range 9)] [[r c] k]))
        ]
    {:x cols :s (into #{} rows)}
    )
  )

(defn to-sudoku-solution [cover-solution]
  (into {}
        (map
          (fn [cols]
            (let [cols-row (filter #(< % 81) cols)
                  col-row (first cols-row)
                  r (quot col-row 9)
                  r-val (mod col-row 9)
                  cols-col (filter #(< 80 % (* 2 81)) cols)
                  col-col (- (first cols-col) 81)
                  c (quot col-col 9)
                  c-val (mod col-col 9)
                  ]
              [[r c] r-val]
              )
            )
          cover-solution))
  )

(defn sudoku-cells [cells]
  (let [{:keys [x s]} (sudoku-to-cover)
        cover-solutions (general-exact-cover x #{} s (map sudoku-to-row cells) true)
        sudoku-solutions (map to-sudoku-solution cover-solutions)]
    (into #{} sudoku-solutions)
    )
  )

(defn fill-matrix [matrix r c]
  (let [matrix (if (< (count matrix) (inc r))
                 (into matrix (repeat (- (inc r) (count matrix)) []))
                 matrix
                 )
        row (nth matrix r)
        row (if (< (count row) (inc c))
              (into row (repeat (- (inc c) (count row)) 0))
              row
              )
        ]
    (assoc matrix r row)
    )
  )

(defn cells-to-matrix [cells init-matrix]
  (reduce
    (fn [acc [[r c] k]]
      (let [matrix (fill-matrix acc r c)]
        (assoc matrix r (assoc (nth matrix r) c (inc k))))
      )
    init-matrix
    cells)
  )

(defn sudoku-matrix-to-cells [matrix]
  (map-indexed
    (fn [r row]
      (into {}      (filter (complement nil?) (map-indexed
                                                (fn [c cell]
                                                  (if (< 0 cell 10) [[r c] (dec cell)])
                                                  )
                                                row))
            )      )
    matrix)
  )

(defn sudoku-matrix [matrix]
  (let [cells-solutions (sudoku-cells (into {} (sudoku-matrix-to-cells matrix)))]
    (into #{}
          (map
            #(cells-to-matrix % matrix)
            cells-solutions)
          )
    )
  )

(defn -main []
  )
