# itch-publish: acceptance scenarios

1. The uploaded HTML or native artifact launches from the actual project page. Record the fixture, action, expected result and observed result.
2. Nested zip roots, missing executable permissions and channel mismatch are detected. Record the fixture, action, expected result and observed result.
3. Draft visibility, pricing and public release follow the user's authorized scope. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
