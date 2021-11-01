(ns algos.permutation-test
  (:require [clojure.test :refer :all]
            [algos.permutation :as permutation]))

(deftest permutation
  (doseq [td [
              [[1 2 3] [1 3 2] "start"]
              [[3 2 1] nil "last"]
              [[1 3 2]  [2 1 3] "middle"]
              ]]
    (is (= (second td) (permutation/perm-next (first td))) (nth td 2))
    )
  )
