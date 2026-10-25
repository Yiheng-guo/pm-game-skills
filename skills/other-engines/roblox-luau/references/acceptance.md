# roblox-luau: acceptance scenarios

1. Server and client scripts run in their intended containers. Record the fixture, action, expected result and observed result.
2. Untrusted client arguments are type- and range-checked on the server. Record the fixture, action, expected result and observed result.
3. Player removal disconnects per-player connections and clears owned state. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
