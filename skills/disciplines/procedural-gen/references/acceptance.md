# procedural-gen: acceptance scenarios

1. A published seed reconstructs the same playable layout and spawn choices. Record the fixture, action, expected result and observed result.
2. An explicit seed set checks connectivity, spawn safety and objective reachability. Record the fixture, action, expected result and observed result.
3. Generation has an attempt cap and a known-playable fallback. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
