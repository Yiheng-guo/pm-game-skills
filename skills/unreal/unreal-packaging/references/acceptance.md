# unreal-packaging: acceptance scenarios

1. A packaged build opens the configured default map and accepts input. Record the fixture, action, expected result and observed result.
2. Missing cooked assets, case-sensitive paths and shipping-only configuration are checked. Record the fixture, action, expected result and observed result.
3. Platform prerequisites and signing remain separate from source publication. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
