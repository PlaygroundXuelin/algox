(ns algos.move-zeros)

(defn move-zeros [nums]
  (let [n (count nums)
        {:keys [nums next]} (reduce
          (fn [{:keys [nums next] :as result} i]
            (let [ni (nth nums i)]
              (if (zero? ni)
                result
                {:nums (assoc nums next ni) :next (inc next)}
                )
              )
            )
          {:nums nums :next 0}
          (range n))]
      (reduce
        #(assoc %1 %2 0)
        nums
        (range next n))
    )
  )
