## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.

## 2025-02-01 - Consolidate GitHub Actions Jobs to Reduce Overhead

**Learning:** Each job in a GitHub Actions workflow has significant overhead due to runner provisioning and initialization. For `pull_request` events, using built-in variables like `${{ github.head_ref }}` can eliminate the need for a separate 'setup' job to get the branch name.

**Action:** Always check if information retrieved in a separate job is already available via GitHub context variables. Consolidating jobs can save 10-30 seconds of execution time per workflow run.