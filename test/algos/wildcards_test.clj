(ns algos.wildcards-test
  (:require
    [algos.wildcards :as w]
    [clojure.test :refer [deftest is]]))

(deftest matches
  (is (w/matches "" "") "empty pattern, empty string")
  (is (not (w/matches "x" "")) "empty pattern")
  (is (w/matches "" "*") "* pattern, empty string")
  (is (w/matches "x" "*") "* pattern, x")
  (is (w/matches "xy" "*") "* pattern, xy")
  (is (not (w/matches "" "?")) "? pattern, empty string")
  (is (w/matches "x" "?") "? pattern, x")
  (is (not (w/matches "xy" "?")) "? pattern, xy")
  (is (not (w/matches "acdcb" "a*c?b")) "a*c?b pattern, string acdcb")
  (is (w/matches "adceb" "*a*b") "*a*b pattern, string adceb")
  )