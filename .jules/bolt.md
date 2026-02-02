## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.

## 2025-01-24 - Consolidate GitHub Actions Jobs for Efficiency

**Learning:** Job overhead in GitHub Actions (spinning up runners, setting up environments) is a measurable performance cost. Consolidation of small, single-purpose jobs like 'setup' into dependent jobs by using built-in environment variables (e.g., `${{ github.head_ref }}`) can save 30-60 seconds per workflow run.

**Action:** Always check if external actions used for metadata (like branch names) can be replaced with native GitHub context variables to reduce job count and execution time.
