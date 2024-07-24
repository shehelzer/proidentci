import unittest
import time

class TestRateLimiter(unittest.TestCase):

    def setUp(self):
        self.rate_limiter = RateLimiter(max_requests=5, period=10)  # Allow 5 requests per 10 seconds

    def test_allow_requests_within_limit(self):
        current_time = time.time()
        for _ in range(5):
            self.assertTrue(self.rate_limiter.allow_request(current_time))

    def test_reject_requests_exceeding_limit(self):
        current_time = time.time()
        for _ in range(5):
            self.rate_limiter.allow_request(current_time)
        self.assertFalse(self.rate_limiter.allow_request(current_time))  # 6th request should be rejected

    def test_allow_requests_after_period_reset(self):
        current_time = time.time()
        for _ in range(5):
            self.rate_limiter.allow_request(current_time)
        
        # Simulate waiting for the period to reset
        time.sleep(11)  # Wait for more than the period (10 seconds)
        new_time = time.time()

        self.assertTrue(self.rate_limiter.allow_request(new_time))  # New request after period should be allowed

if __name__ == '__main__':
    unittest.main()
