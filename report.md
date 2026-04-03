# Report

## Business Use Case

This project focuses on turning raw meeting notes into a short meeting summary and a list of action items. The target user is a project manager or team lead who needs to quickly review what happened in a meeting and follow up on next steps. This is a useful task to automate because meeting notes are often messy, repetitive, and time-consuming to rewrite into a clear business update.

## Model Choice

I used Gemini (model ID `gemini-2.5-flash`) through the Google GenAI Python SDK. I chose this model because it was easy to access through Google AI Studio, worked well with simple Python integration, and was sufficient for a lightweight prototype. Since the assignment focused on building and evaluating a small workflow rather than optimizing across many providers, I chose one model and concentrated on improving the prompt design.

## Baseline vs. Final Design

The baseline version of the prompt asked the model to produce a short meeting summary and a list of action items. This version produced a generally clear response, but it sometimes missed important details from the notes. In the sample test, it identified the action items correctly, but it did not clearly include the planned launch next Tuesday.

The final prompt added a more explicit structure and asked for timeline or key decision information in addition to the summary and action items. This improved the output by making it more complete and easier to review. In the revised result, the model still captured the action items, but it also included the launch plan as part of the timeline. This made the output more useful for business follow-up.

## Remaining Failure Cases and Human Review

This prototype still needs human review in several cases. If the notes are incomplete, vague, or contain legal, contractual, or sensitive issues, the model may miss context or present uncertain information too confidently. It may also struggle when owners or deadlines are only implied rather than clearly stated. For those reasons, the output should be treated as a first draft rather than a final business record.

## Deployment Recommendation

I would recommend this workflow only as a draft-generation tool with human review. It could be useful for internal productivity, especially for routine meetings where the notes are clear and factual. However, it should not be deployed as a fully automated system for high-stakes communication without review controls. A human should still check the summary, confirm action items, and verify any timeline or decision-related details before sharing the result.
