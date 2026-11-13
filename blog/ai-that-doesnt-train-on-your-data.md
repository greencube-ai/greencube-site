# Which AI doesn't train on your chats? We checked 9 (October 2026)

> Does ChatGPT, Gemini, Claude, Copilot, Perplexity, NotebookLM, Mistral, DeepSeek or Meta AI train on what you type? What each one's own help pages say, how to turn it off, and what the switch doesn't cover.

Canonical: https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data  
Published: 2026-10-18  
Author: Hector Gras

Most of them do, unless you switch it off. Of 9 popular AIs we checked, 5 train on what you type by default on a free personal account: ChatGPT, Perplexity, Mistral, DeepSeek and Meta AI. Gemini and Claude depend on a setting, NotebookLM says it doesn't unless you send feedback, and Microsoft's new Copilot app doesn't say.

Turning training off is worth doing, but it doesn't make a chat private, for reasons I'll get to below. I build GreenCube, an AI that runs on your own PC, so weigh my view with that in mind. Everything about the other services comes from their own help pages, linked in the table.

## What each one says (checked 18 October 2026)

We read each company's own help pages for a free personal account. Work and school accounts usually have stricter rules: on most of these services they're left out of training by default. Policies change often, so we check again every month.

| AI | Trains on your chats? | How to turn it off | What the switch doesn't cover |
| --- | --- | --- | --- |
| **ChatGPT** (Free, Go, Plus, Pro) | **Yes, by default** | Settings → Data controls → "Improve the model for everyone" off. Temporary Chats aren't used. | Thumbs up or down feedback: the whole conversation may be used. [OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) |
| **Gemini** | **Yes, while "Keep Activity" is on** | Turn off Keep Activity. Future chats aren't used to train, but are still kept 72 hours. | Chats a human reviewer has read are kept up to 3 years, even if you delete your activity. [Google](https://support.google.com/gemini/answer/13594961?hl=en) |
| **Claude** (Free, Pro, Max) | **Only if you allow it** (you choose when you sign up) | Privacy settings → model improvement off. | If allowed, chats are kept up to 5 years; turning it off later doesn't remove data already used. [Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms) |
| **NotebookLM** (Gemini Notebook) | **No**, unless you send feedback | Nothing to switch off. Don't use thumbs up or down on sensitive notes. | With feedback, your uploads and questions can be reviewed and kept up to 3 years. [Google](https://support.google.com/notebooklm/answer/17004255?hl=en) |
| **Microsoft Copilot** (new app since 18 Aug 2026) | **Not stated** for the new app | Microsoft's training opt-out is described only for the old app. The new app's privacy controls list no training switch. | Check the app's own settings. [Microsoft](https://support.microsoft.com/en-us/privacy/microsoft-copilot/overview) |
| **Perplexity** (Free, Pro, Max) | **Yes, by default** | Settings → Preferences → "AI data retention" off. | Only stops data from then on; earlier data isn't removed. [Perplexity](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity) |
| **Mistral Le Chat** (free) | **Yes, by default** | Settings → Privacy → "Allow your interactions to be used to train our models" off. | Thumbs up or down feedback is used whatever you choose. [Mistral](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) |
| **DeepSeek** | **Yes, by default** (de-identified) | Turn off "Improve the model for everyone". | [DeepSeek](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html) |
| **Meta AI** | **Yes**, your questions to Meta AI are used | In the EU, object with Meta's form (from the app or the email Meta sent). | The objection covers the account you're logged into and others in the same Accounts Centre. [Meta](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/) |
| **GreenCube** (runs on your PC) | **No**, your chats never reach us | Nothing to switch off. | Online search, which starts off every time, sends search terms to search engines. [GreenCube](https://legal.greencube.app/privacy) |

## What "turn off training" doesn't do

The switch covers one thing: whether what you type from now on goes into training. Three things slip past it.

The first is feedback. Clicking thumbs up or down often sends the whole conversation for review, even with training off. OpenAI, Mistral and Google (for NotebookLM and Gemini) all say so. If a chat holds something sensitive, don't rate it.

The second is human review. Gemini uses human reviewers while Keep Activity is on, and keeps the chats they've read for up to 3 years, disconnected from your account, even if you delete your activity.

The third is what's already been used. Anthropic and Perplexity both say data already in training isn't removed when you switch off. So if you're going to turn it off, do it before you paste in your notes, not after.

## The only way your words stay on your computer

Every service above runs the AI on its own servers, so what you type has to travel there, whatever the training setting says. An AI that runs on your own computer works the other way round. The model is a file on your PC, your chats and documents are stored there, and no company server holds them.

That's how GreenCube works, and its privacy policy says it plainly: "We never receive your chats, files, memories or images." The honest exceptions are that you sign in once to activate it, it downloads the AI and its updates, and if you switch on Online search for something current, it sends search terms built from your question to search engines. Online starts off every time you open the app.

The trade-off is that your computer does the work. On the PCs we measured, it writes at about reading speed on an 8 GB laptop and many times faster on a gaming PC. You can [check what yours can run](https://blog.greencube.app/blog/can-my-pc-run-ai#checker).

## How we checked

On 18 October 2026 we read each company's own help center and privacy pages for a free, personal, adult account, not news articles or reviews, and linked the page each row comes from. Where a company's current pages don't answer the question, as with Microsoft's new Copilot app, we say so instead of guessing. We'll check again every month and update the date at the top.

## FAQ

### Does ChatGPT train on my chats?

Yes, by default on Free, Go, Plus and Pro. You can switch off "Improve the model for everyone" in Settings, Data controls, but if you give a thumbs up or down, OpenAI may still use that whole chat.

### Which AI doesn't use my data for training?

Of the 9 we checked, NotebookLM says it doesn't train on your uploads unless you send feedback, and Claude only does if you allow it. An AI that runs on your own computer, like GreenCube, never sends your chats anywhere to train on.

### Does turning off training make an AI private?

Not completely. Feedback you give can still be used, some companies keep chats for human review (Gemini keeps reviewed ones up to 3 years), and what was already used for training isn't removed.

### Is there an AI that keeps my chats on my computer?

Yes, one that runs locally, like GreenCube. Besides signing in once and downloading the AI and its updates, the only thing that goes online is an optional web search, which sends just the search terms and starts off every time.
