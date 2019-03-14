def coin_sum(coins, total):
	dp = [1] + [0] * total
	for coin in coins:
		for i in range(coin, total + 1):
			dp[i] += dp[i - coin]
	return dp[total]

def solve():
	print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 1000))

if __name__ == '__main__':
	solve()