(ns algos.polindrom-test
  (:require [clojure.test :refer :all]
            [algos.polindrome :as polin]))

(deftest find-naive
  (doseq [[f f-name] [[polin/find-naive "naive"] [polin/find-manacher "manacher"]]]
    (is (= 1 (f "abcde")) f-name)
    (is (= 2 (f "xaabbccd")) f-name)
    (is (= 3 (f "xaabaccd")) f-name)
    (is (= 4 (f "xaabxyyxabc")) f-name)
    )
  )
