# Evaluation Set

## Case 1 - Normal case
**Input:**
Project sync meeting notes:
- Final website draft is almost done
- Sarah will send the final design files by Wednesday
- Kevin will update the homepage copy by Friday
- Team plans to launch next Tuesday

**What a good output should do:**
A good output should provide a short and clear summary of the meeting and list the action items with the correct owners and deadlines.

---

## Case 2 - Normal case
**Input:**
Marketing team meeting:
- Social media campaign performed well last week
- Need to increase budget for Instagram ads
- Emily will prepare a new budget proposal
- Jason will review ad performance data before Thursday

**What a good output should do:**
A good output should summarize the main discussion and identify the follow-up tasks clearly.

---

## Case 3 - Edge case
**Input:**
Weekly check-in notes:
- Team discussed delays in vendor response
- Might need to move the deadline
- Someone should follow up with procurement
- Budget issue still not resolved

**What a good output should do:**
A good output should avoid making up names or deadlines that are not provided. It should mention uncertainty clearly.

---

## Case 4 - Likely failure or human review case
**Input:**
Client call notes:
- Client seemed unhappy with the current progress
- They mentioned legal concerns about data sharing
- The team may need to revise the contract
- Follow-up email should be sent soon

**What a good output should do:**
A good output should summarize the discussion carefully and flag that legal or contract-related issues may require human review. It should not invent legal advice.

---

## Case 5 - Messy input case
**Input:**
Notes:
- launch maybe delayed
- ask finance about budget
- tom? not sure
- need update for leadership
- next meeting monday maybe 2pm

**What a good output should do:**
A good output should organize the messy notes into a readable summary and action items, while clearly showing uncertainty where the notes are unclear.