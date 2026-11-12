# Claude usage limit in 2026: the 5-hour and weekly limits, explained

> How Claude's usage limits work in November 2026: a limit every 5 hours and one every week on Free, Pro and Max, no 5-hour limit on verified Ultra. What uses it up, when it resets, and what to do when you hit it.

Canonical: https://blog.greencube.app/blog/claude-usage-limit  
Published: 2026-11-06  
Author: Hector Gras

Claude has two usage limits: one that resets every 5 hours and one that resets once a week. Free, Pro and Max have both. The $200 Ultra plan has only the weekly one, once your account is verified. Anthropic doesn't publish how many messages any plan gets, because long chats, big files and the stronger models use the limit up faster.

## The limits, plan by plan

|  | Price | Every 5 hours | Every week |
| --- | --- | --- | --- |
| **Free** | $0 | Limited | Limited |
| **Pro** | $20 a month ($17 a month paid yearly) | 1x | 1x |
| **Max** | $100 a month | 5x Pro | 5x Pro, plus a separate weekly limit for the Fable model |
| **Ultra** (was Max 20x) | $200 a month | None, for verified accounts | 10x Pro |

This comes from Anthropic's [pricing page](https://claude.com/pricing) and its help pages on the [Pro](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan), [Max](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) and [Ultra](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan) plans, checked on 6 November 2026. Prices are in US dollars, before tax. "1x" and "5x" are Anthropic's own terms: it describes the limits as multiples of Pro, never as a number of messages.

### What changed recently

Max 20x is now called Ultra, at the same $200, and subscribers moved over automatically. If "20x" turning into "10x" looks like a cut, it may not be. The old 20x described the 5-hour window, and reports of the 30 October change say the weekly allowance stayed the same ([Magica](https://magica.com/news/anthropic-removes-five-hour-limit-ultra-plan)). The new name describes what the week actually holds.

Ultra also dropped the 5-hour limit, but only once Anthropic has verified your account. Until then, "a temporary limit applies" ([Anthropic Help Center](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)). The weekly limit stays on every plan.

## What uses up your limit faster

Anthropic's help page lists what counts: "the length and complexity of your conversations, the features you use, which Claude model you're chatting with, and the effort level you've selected" ([Anthropic Help Center](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits)).

Long chats are the big one. Every new message is read together with the conversation before it, and long conversations that trigger Claude's automatic context management "consume more of your usage limit", in Anthropic's words. Big files work the same way: the longer the file you attach, the fewer messages you get. The strongest model and high effort settings also use more per message.

Then there's Claude Code. It shares one limit with the Claude app and Claude Desktop, so a long coding session can use up the week you were saving for chat.

## When it resets

The session limit resets every five hours. The weekly limit resets "at a fixed time each week that is assigned to your account", and that time stays the same whenever you started your subscription ([Anthropic Help Center](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)). Anthropic doesn't publish the time, but you can see your own in Claude's settings, under Usage.

Anthropic also says it "may adjust usage limits at our discretion to manage capacity". So a limit you hit easily one week may feel different the next.

## What to do when you hit it

1. Wait for the reset. If it's the 5-hour limit, it's hours away. If it's the weekly one, check the day in your Usage settings.
2. Start a new chat, and copy over the two or three lines that matter instead of dragging a long conversation along.
3. Send smaller files: the chapter you need, not the whole book.
4. Use a lighter model for simple questions and save the top one for the hard ones.
5. Pay as you go. Pro, Max and Ultra can turn on usage credits to keep going past the limit. They're "billed at standard API rates" ([Anthropic Help Center](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)), so the cost depends on how much you send.
6. Upgrade, if you hit the limit every week. Max gives 5 times Pro's usage, Ultra 10 times Pro's weekly usage.

## Or move the everyday work to your own PC

Usage limits exist because every message runs on Anthropic's servers, and someone pays for those. An AI that runs on your own computer has no counter, because there's no server to pay for.

That's what [GreenCube](https://greencube.app/) does, and since I build it, weigh this part with that in mind. You download it once, and it chats, reads your PDFs and makes pictures (those need 12 GB of RAM) with no 5-hour or weekly limit, even with no internet.

|  | Claude Pro | AI on your own PC (GreenCube) |
| --- | --- | --- |
| Limit every 5 hours | Yes | None |
| Limit every week | Yes | None |
| Files and PDFs | Count against the limit | No cap |
| Works with no internet | No | Yes, after one download |
| How smart | One of the strongest AIs there is | Small models (Gemma 4) that fit on a normal PC: good for studying, writing and everyday questions, weaker on hard reasoning and big code |
| Speed | Fast on any device | Depends on your PC: 5 to 7 tokens a second on an 8 GB laptop, 14 to 18 on a 16 GB laptop, 37 to 76 on most gaming PCs in our tests |
| Price | $20 a month | €9.99 once |

To be clear, for a hard bug in a big codebase or a long piece of careful reasoning, Claude is the stronger tool, and a small model on a laptop won't replace it. Where a local AI helps is the everyday volume that eats your limit: summarising notes, rewording, quick questions, quizzing yourself on a PDF. Move that to your PC and keep Claude's limit for the work that needs it.

Not sure your PC can run one? [Check it here](https://blog.greencube.app/blog/can-my-pc-run-ai). For the other big chat app, see [ChatGPT's free limits](https://blog.greencube.app/blog/chatgpt-free-limits), and for every option with no limits at all, [unlimited AI, compared](https://blog.greencube.app/blog/unlimited-ai).

## FAQ

### How many messages can I send on Claude?

Anthropic doesn't publish a number for any plan. Its help pages say the number of messages varies with message length, the files you attach, the length of the conversation and the model or feature you use.

### When does the Claude limit reset?

There are two limits. The session limit resets every five hours. The weekly limit resets at a fixed day and time each week that Anthropic assigns to your account; it stays the same no matter when you started your subscription. You can see both in Claude's settings under Usage.

### Does Claude Code share the limit with the Claude app?

Yes. Anthropic's help page says that claude.ai, Claude Code and Claude Desktop all count towards the same usage limit.

### What is Claude Ultra?

It is the new name of the Max 20x plan. It costs $200 a month, includes 10 times Pro's weekly usage and has no five-hour limit for verified accounts. Max (the old Max 5x) is still $100 a month with both limits.

### Is there an AI with no usage limit at all?

An AI that runs on your own PC has no counter, because no server is paying per message. GreenCube is one: no caps on chats, files or pictures, works without internet, €9.99 once. The trade-off is that it runs smaller models than Claude, and its speed depends on your PC.
