# godot-multiplayer: acceptance scenarios

1. Two separate peers connect and authoritative state converges. Record the fixture, action, expected result and observed result.
2. Disconnect, invalid RPC payload and unauthorized sender are rejected or recovered. Record the fixture, action, expected result and observed result.
3. Reconnection cannot leave duplicate player nodes or grant rewards twice. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
