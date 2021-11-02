(ns algos.move-zeros-test
  (:require [clojure.test :refer :all]
            [algos.move-zeros :as move-zeros]))

(deftest move-zeros
  (is (= [] (move-zeros/move-zeros [])))
  (is (= [1] (move-zeros/move-zeros [1])))
  (is (= [0] (move-zeros/move-zeros [0])))
  (is (= [1 0] (move-zeros/move-zeros [0 1])))
  (is (= [1 0] (move-zeros/move-zeros [1 0])))
  (is (= [1 2 2 1 0 0] (move-zeros/move-zeros [1 0 2 0 2 1])))
  (is (= [1 2 3 2 0 0 0] (move-zeros/move-zeros [0 1 2 0 3 0 2])))
  )