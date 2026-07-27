import math
import numpy as np

def bs_mc_call(S0, K, T, r, sigma, M, seed):
    # Monte Carlo price of a European call under risk-neutral geometric Brownian motion.
    # Sample the terminal price directly (no path discretization needed):
    #   for each of M paths draw Z ~ N(0,1) and set
    #     S_T = S0 * exp((r - 0.5*sigma**2)*T + sigma*sqrt(T)*Z)
    #   payoff = max(S_T - K, 0)
    #   price  = exp(-r*T) * mean(payoffs)
    # Seed your RNG with `seed` so the result is deterministic given the inputs.
    # Return the estimated price as a float.
    # your code here
    
    rng=np.random.default_rng(seed)
    Z=rng.standard_normal(M)
    ST=S0*np.exp((r-0.5*sigma**2)*T+sigma*np.sqrt(T)*Z)
    payoff=np.maximum(ST-K,0.0)
    return float(np.exp(-r*T)*payoff.mean())


if __name__=="__main__":

    print(bs_mc_call(100, 100, 1, 0.05, 0.2, 500000, 7))
    
