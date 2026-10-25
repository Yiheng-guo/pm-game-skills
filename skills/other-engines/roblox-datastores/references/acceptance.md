# roblox-datastores: acceptance scenarios

1. A separate test place round-trips a versioned player record. Record the fixture, action, expected result and observed result.
2. Throttling, API failure and concurrent sessions cannot overwrite a newer authoritative save. Record the fixture, action, expected result and observed result.
3. No client can write authoritative progression and tests avoid live-player records. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
