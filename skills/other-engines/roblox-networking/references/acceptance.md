# roblox-networking: acceptance scenarios

1. A valid client request yields one server-authoritative result. Record the fixture, action, expected result and observed result.
2. Malformed, replayed and rate-excess requests cannot create state changes. Record the fixture, action, expected result and observed result.
3. The protocol has explicit ownership and handles disconnect/reconnect. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
