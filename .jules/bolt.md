## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.