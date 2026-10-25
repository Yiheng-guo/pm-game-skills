# card-game: acceptance scenarios

1. A legal turn pays cost once, resolves effects in order and reaches the next actor. Record the fixture, action, expected result and observed result.
2. Empty deck, duplicate effects and invalid targets cannot duplicate cards or resources. Record the fixture, action, expected result and observed result.
3. A seeded replay produces the same zones and winner. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
