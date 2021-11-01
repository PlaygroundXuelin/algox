(ns algos.permutation)

(defn perm-next [p]
  (let [n (count p)]
    (reduce
      (fn [p k]
        (let [i (- n 2 k)
              pi (nth p i)
              pi1 (nth p (inc i))]
          (if (> pi pi1)
            (if (zero? i) nil p)
            (let [next-pi (apply min (filter #(> % pi) (subvec p (inc i) n)))
                  tail (filter #(not (= % next-pi)) (subvec p i n))
                  tail (sort tail)]
              (reduced (into (subvec p 0 i) (into [next-pi] tail)))
              )
            )
          )
        )
      p
      (range (dec n))
      )
    )
  )

(defn all-perms [n]
  (loop [p (into [] (range n))]
    (if (nil? p) nil
                 (do
                   (println p)
                   (recur (perm-next p)))
                 )
    )
  )

(defn -main []
  (all-perms 3)
  )
