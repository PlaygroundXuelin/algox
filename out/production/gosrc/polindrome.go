package gosrc

func findPolineNext(str string, mc, i int) int {
	for tmp := mc + 1; tmp <= 2*i+1; tmp++ {
		left := tmp / 2
		if tmp%2 == 0 {
			left--
		}
		right := tmp/2 + 1
		mc = tmp
		if right > i {
			break
		}
		var mismatch bool
		for right <= i {
			if str[left] != str[right] {
				mismatch = true
				break
			}
			right++
			left--
		}
		if !mismatch {
			break
		}
	}
	return mc
}

func Polinedrome(str string) int {
	n := len(str)
	if n <= 1 {
		return n
	}

	mc := 1
	max := 1
	i := mc/2 + 1
	for mc < 2*n-2 && i < n {
		ch := str[i]
		if mc%2 == 0 {
			// center is char
			centerI := mc / 2
			delta := i - centerI
			checkIndex := centerI - delta
			if str[checkIndex] == ch {
				currMax := 2*delta + 1
				if currMax > max {
					max = currMax
				}
				if checkIndex == 0 {
					mc = findPolineNext(str, mc, i)
					i = mc/2 + 1
				} else {
					i++
				}
			} else {
				mc = findPolineNext(str, mc, i)
				i = mc/2 + 1
			}
		} else {
			centerRight := mc/2 + 1
			delta := i - centerRight
			checkIndex := centerRight - 1 - delta
			if str[checkIndex] == ch {
				currMax := 2 * (delta + 1)
				if currMax > max {
					max = currMax
				}
				if checkIndex == 0 {
					mc = findPolineNext(str, mc, i)
					i = mc/2 + 1
				} else {
					i++
				}
			} else {
				mc = findPolineNext(str, mc, i)
				i = mc/2 + 1
			}
		}
	}
	return max
}
