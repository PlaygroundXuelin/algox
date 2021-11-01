(ns algos.regex)

(defn matches-index [s s-index p p-index]
  (let [s-done (= s-index (count s))
        p-len (count p)
        p-done (= p-index p-len)]
    (cond
      (and s-done p-done) true
      s-done
      (cond
        (= (inc p-index) p-len) false
        (= (nth p (inc p-index)) \*) (matches-index s s-index p (+ 2 p-index))
        :else false
        )
      p-done false
      :else
      (let [s-ch (nth s s-index)
            p-ch (nth p p-index)
            p-ch-any (= p-ch \.)
            p-next (inc p-index)]
        (cond
          (or (= s-ch p-ch) p-ch-any)
          (cond
            (= p-next p-len) (matches-index s (inc s-index) p p-next)
            (= (nth p p-next) \*)
            (if (matches-index s s-index p (inc p-next))
              true
              (matches-index s (inc s-index) p p-index)
              )
            :else
            (matches-index s (inc s-index) p p-next)
            )
          (= p-next p-len) false
          (= (nth p p-next) \*) (matches-index s s-index p (+ 2 p-index))
          :else false
          )
        )
      )
    )
  )

(defn matches
  "Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
  Matches any single character '*' Matches zero or more of the preceding element.
  The matching should cover the entire input string (not partial).
  "
  [s p]
  (matches-index s 0 p 0)
  )