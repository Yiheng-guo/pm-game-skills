# save-systems: acceptance scenarios

1. Round-trip save/load reproduces authoritative state and unlocks. Record the fixture, action, expected result and observed result.
2. Malformed, truncated, older and future-version data recover without overwriting the last good save. Record the fixture, action, expected result and observed result.
3. Storage denial is visible but does not prevent a new local game. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
