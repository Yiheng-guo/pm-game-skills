# roblox-studio-workflow: acceptance scenarios

1. The change survives the canonical Studio or Rojo save/sync cycle. Record the fixture, action, expected result and observed result.
2. Repeated sync and multi-client play preserve unrelated project structure. Record the fixture, action, expected result and observed result.
3. Generated subtrees are changed through their owner rather than hand-edited. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
