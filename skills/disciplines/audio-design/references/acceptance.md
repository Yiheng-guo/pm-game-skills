# audio-design: acceptance scenarios

1. Music, effects and UI volumes respond independently without clipping. Record the fixture, action, expected result and observed result.
2. Muted startup and denied audio activation leave gameplay usable. Record the fixture, action, expected result and observed result.
3. Repeated scene entry does not multiply voices or leak audio nodes. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
