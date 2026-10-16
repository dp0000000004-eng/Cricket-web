from rest_framework.throttling import UserRateThrottle

class MatchesThrottle(UserRateThrottle):
    scope = 'two'