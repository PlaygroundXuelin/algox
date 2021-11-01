(ns algos.regex-test
  (:require
    [algos.regex :as ar]
    [clojure.test :refer :all]))

(deftest matches
  (is (= false (ar/matches "aa" "a")))
  (is (= true (ar/matches "aa" "a*")))
  (is (= true (ar/matches "ab" ".*")))
  (is (= true (ar/matches "aab" "c*a*b")))
  (is (= false (ar/matches "mississippi" "mis*is*p*.")))
  )
