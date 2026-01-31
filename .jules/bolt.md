## 2024-07-11 - Optimize External API Calls with Caching

**Learning:** External API calls, even for assets like images, can be a performance bottleneck. The `github-readme-stats` service allows for a `cache_seconds` parameter, which can significantly improve load times for repeat visitors by leveraging browser caching.

**Action:** When encountering external media or API calls in the future, investigate if the service provides caching parameters. A simple change can lead to a measurable performance improvement with minimal effort.

## 2024-07-25 - Consolidate GitHub Actions Jobs

**Learning:** Each job in a GitHub Actions workflow incurs overhead due to runner provisioning. Small utility jobs (like getting a branch name) should be consolidated into the main jobs that need the data, or replaced with built-in variables like `${{ github.head_ref }}`.

**Action:** Minimize the number of jobs in a workflow by merging simple logic into dependent jobs. Always prefer built-in context variables over external actions when possible.