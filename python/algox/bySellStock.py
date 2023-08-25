def buy_sell_stock(prices)->float:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
 in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Analysis:
    Naive solution is O(n^2).
    Optimize: O(n)
      fi is max profit for a buy/sell in range 0..i. fi is 0 if pi is non-increasing in the range.
      maintain curr_min so far.
      if pi+1 - curr_min > fi, fi+1 = pi+1 - min, else fi+1 = fi. curr_min = min(min, pi+1)
    :param prices:
    :return:
    """
    curr_min = 1000000
    max_profit = 0
    for p in prices:
        if p - curr_min > max_profit:
            max_profit = p - curr_min
        curr_min = min(curr_min, p)
    return max_profit


if __name__ == "__main__":
    # p = [7,1,5,3,6,4]
    p = [7,6,4,3,1]
    max_profit = buy_sell_stock(p)
    print("max profit: ", max_profit)
