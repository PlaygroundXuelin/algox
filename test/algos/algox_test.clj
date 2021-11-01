(ns algos.algox-test
  (:require
    [algos.algox :as algox]
    [clojure.pprint :as pprint]
    [clojure.test :refer :all]))

(deftest algox
  (doseq [[cover-f f-name] [[algox/exact-cover "exact-cover"] [algox/exact-cover-2 "exact-cover-2"]]]
    (let [n #{} o #{1 3} p #{2 3} e #{2 4} x #{1 2 3 4}]
      (is (= #{#{o e}} (cover-f x #{n o p e})) f-name))

    (let [x #{1 2 3 4 5 6 7}
          a #{1 4 7}
          b #{1 4}
          c #{4 5 7}
          d #{3 5 6}
          e #{2 3 6 7}
          f #{2 7}]
      (is (= #{#{b d f}} (cover-f x #{a b c d e f})) f-name)
      )
    )
  )

(deftest queens
  (is (= #{#{[1 3] [2 0] [3 2] [0 1]}
           #{[1 0] [2 3] [0 2] [3 1]}} (algox/queens 4)))
  (is (= 92 (count (algox/queens 8))))
  )

(deftest sudoku
  (let [solutions
        (algox/sudoku-matrix
          [[0 6 0 3 0 0 8 0 4]
           [5 3 7 0 9]
           [0 4 0 0 0 6 3 0 7]
           [0 9 0 0 5 1 2 3 8]
           []
           [7 1 3 6 2 0 0 4 0]
           [3 0 6 4 0 0 0 1]
           [0 0 0 0 6 0 5 2 3]
           [1 0 2 0 0 9 0 8]
           ])]
    (is (=
          #{[[2 6 1 3 7 5 8 9 4]
             [5 3 7 8 9 4 1 6 2]
             [9 4 8 2 1 6 3 5 7]
             [6 9 4 7 5 1 2 3 8]
             [8 2 5 9 4 3 6 7 1]
             [7 1 3 6 2 8 9 4 5]
             [3 5 6 4 8 2 7 1 9]
             [4 8 9 1 6 7 5 2 3]
             [1 7 2 5 3 9 4 8 6]]}
          solutions))
    )
  )
