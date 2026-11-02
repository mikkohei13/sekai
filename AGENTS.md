## Development principles

- Default to the simplest working solution. If a simpler approach would only partly meet the request, ask the user before using it, and explain what it would leave out.
- This is one-person app, so avoid premature optimization.
- Add unit tests to ./tests for the most important features only.

- This app is in development, so no backwards compatibility or migration scripts are needed.

## Technical principles

See README.md for the architecture.

- Use UV for package management.
- Use semantic HTML. Use native elements as intended: <a> for navigation, <button> for actions, <form> with a <label> on every input, landmarks (<nav>, <main>), headings in order, and <table> for tabular data. Don't make <div>s clickable. Use ARIA only when no native element fits. 
- Every page and meaningful view state (filters, sorting, pagination, tabs, selected item) has its own URL in the path or query string. Opening that URL fresh shows the same view. When JS changes state, update the URL with the History API.
- Rule of thumb: Business logic in Python. JavaScript handles UI interaction only and never repeats business rules.
