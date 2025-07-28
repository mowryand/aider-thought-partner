Project Summary: “Thought‑Partner Mode” for Aider
=====

Overview:
-----
I envision a new /thought‑partner mode that shifts Aider's behavior: rather than generating code or edits, it engages in Socratic-style questioning—inquiring, clarifying, and co‑exploring user goals before any actionable plan or coding begins.

Current Modes & Workflow:
-----
Aider provides built-in chat modes—code, ask, architect, and help—where:
- code mode edits files directly,
- ask mode discusses and answers questions without modifying code,
- architect mode pairs reasoning (planning) and editing via separate LLM roles

My /thought-partner mode would be analogous to ask, but proactive: it asks framing and goal-setting questions to build higher precision in feature planning.

Custom Mode Vision:
-----
- Trigger: Activated with /thought-partner or sticky via /chat-mode thought-partner.
- Behavior: The AI deliberately refrains from creating code; instead it asks guiding questions (e.g. “What's the primary user need you're solving?”, “Why feature X matters now?”), gradually building a shared context before feature planning begins.
- Outcome: A structured dialog that surfaces user motivations, constraints, desired scope, edge cases—laying the groundwork for eventual feature design and implementation.

Technical Plan:
-----
1. Fork the Aider repository and set up a local branch for the new mode.
2. Implement mode dispatch by adapting logic from existing /ask mode handling in the CLI source.
3. Create a new prompt template: e.g. “When in thought-partner mode, ask clarifying Socratic questions…”
4. Ensure /thought-partner mode routes to reasoning-only behavior (no file edits).
5. Test locally via pip install -e . and python -m aider, switching with /chat-mode thought-partner.
6. Keep the fork synced with upstream, while maintaining the custom mode and template logic.