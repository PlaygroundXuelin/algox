(ns algos.polindrome)

(defn find-by-center
  "Find max polindrom centered at index. If index is negetive, it's the gap before -index - 1"
  [&{:keys [ss index start-len] :or {start-len 0}}]
  (let [[left right len] (if (even? index) [(dec (/ index 2)) (inc (/ index 2)) 1] [(/ (dec index) 2) (/ (inc index) 2) 0])
        ll (count ss)
        start-delta (/ (if (even? start-len) start-len (dec start-len)) 2)
        left (- left start-delta)
        right (+ right start-delta)
        ]
    (loop [left left right right len len]
      (cond
        (or (neg? left) (>= right ll))
        len
        (= (nth ss left) (nth ss right))
        (recur (dec left) (inc right) (+ 2 len))
        :else
        len
        )
      )
    )
  )

(defn find-naive
  "Finds longest polindrome substring length in give str.
  Check longest polindrom centered at each position (index and gap)"
  [ss]
  (reduce
    (fn [result index]
      (let [r (find-by-center {:ss ss :index index})]
        (max r result)
        )
      )
    0
    (range  (dec (* 2 (count ss)))))
  )

(defn manacher
  "Manacher's linear algorithm"
  [ss]
  (reduce
    (fn [{:keys [lens right-most]} index]
      (let [boundary-left (fn [center len]
                            (let [index (/ (if (even? center) center (inc center)) 2)
                                  left-num (/ (if (even? center) (dec len) len) 2)]
                              (- index left-num))
                            )
            [rm-index rm-len] right-most
            mirror-index (if (or (neg? rm-index) (> index (+ rm-index rm-len))) -1 (- rm-index (- index rm-index)))
            start-len (if (neg? mirror-index)
                    (if (even? index) 1 0)
                    (get lens mirror-index))
            start-left (cond (neg? mirror-index) -1
                             :else (boundary-left mirror-index start-len))
            rm-left (boundary-left rm-index rm-len)
            ]
            (cond
              (neg? mirror-index)  (let [len (find-by-center {:ss ss :index index})]
                                     {:lens (merge lens {index len}) :right-most [index len]})
              (> start-left rm-left) {:lens (merge lens {index start-len}) :right-most right-most}
              (< start-left rm-left) {:lens (merge lens {index (- start-len (*  2 (- rm-left start-left)))}) :right-most right-most}
              :else (let [len (find-by-center {:ss ss :index index :start-len start-len})]
                      {:lens (merge lens {index len}) :right-most [index len]})
              )
        )
      )
    {:lens {} :right-most [-1 0]}
    (range (dec (* 2 (count ss)))))
  )

(defn find-manacher [ss]
  (let [{:keys [lens right-most]} (manacher ss)]
    (reduce-kv
      (fn [result index len]
        (max result len)
        )
      0
      lens)
    )
  )
