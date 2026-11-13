# AI flashcards from a PDF: we made them offline and checked every card

> We turned two long chapters into flashcards with an AI on a normal laptop, with no internet: how long it took, how many cards were right when we checked them one by one, where it slips, and the free alternatives.

Canonical: https://blog.greencube.app/blog/flashcards-from-pdf  
Published: 2026-08-22 · Updated: 2026-10-19  
Author: Hector Gras

Yes, you can make AI flashcards from a PDF offline, in about 5 minutes per chapter on a normal laptop. We gave GreenCube two long chapters and asked for exam flashcards, and each came back with 18 cards and a study guide. Then we checked all 36 cards one by one against the original text. Most were right, but not all, and the mistakes bunched up exactly where one chapter jumps between periods.

GreenCube is the app I build, so weigh my opinion with that in mind. Below are the results, the cards it got wrong, and the free alternatives.

## The test

We used two long chapters of the kind that come up in exams: Spain's Second Republic (in Spanish, about 4,800 words) and the Industrial Revolution (in English, about 4,700 words). For each, we typed what a student would type: "make me flashcards of this topic for the exam", in Spanish. For the English chapter we added "in Spanish".

It ran on 19 October 2026 in the real GreenCube app (a test copy of its current version), on a 16 GB laptop with an Intel Core Ultra 5 and its built-in graphics, no graphics card, plugged in and offline. We used the small AI, Gemma 4 E2B, which runs comfortably on a laptop like this.

## The results

| Chapter | Time | Cards | Right | Partly | Wrong | Repeats |
| --- | --- | --- | --- | --- | --- | --- |
| Second Republic (Spanish) | **4 min 57 s** | 18 | **10** | 2 | 5 | 1 |
| Industrial Revolution (English → Spanish) | **4 min 52 s** | 18 | **11** | 4 | 0 | 3 |

The bigger AI does better. We repeated the test with Gemma 4 E4B, the bigger AI GreenCube offers on 16 GB laptops, and got 30 of 36 cards right, 4 partly right, 2 wrong and no repeats.

| Chapter | AI | Right | Partly | Wrong | Repeats |
| --- | --- | --- | --- | --- | --- |
| Second Republic | E2B (small) | 10 | 2 | 5 | 1 |
| Second Republic | E4B (bigger) | **15** | 1 | 2 | 0 |
| Industrial Revolution | E2B (small) | 11 | 4 | 0 | 3 |
| Industrial Revolution | E4B (bigger) | **15** | 3 | 0 | 0 |

We don't publish E4B's time. In this test an app bug made it rewrite the guide several times before the cards. It's fixed for the next version, and we'll time it again then.

"Right" means the card says what the chapter says. "Partly" means it gets the main point but adds or changes a detail. "Wrong" means the chapter says something else. We checked every card by finding the sentence in the original text it came from.

## What it got right

Dates, names and inventions were the most reliable cards. "When was the Spanish Republic proclaimed?" got "14 April 1931". "What did Samuel Crompton invent in 1779?" got "The spinning mule". "Which left-wing coalition won the 1936 election?" got "The Popular Front". (These are translated from the Spanish cards.)

Switching language worked well too. We gave it the Industrial Revolution chapter in English and asked for the cards in Spanish: all 18 came out in Spanish, and none was wrong. That's handy if you study from notes, papers or books in one language and revise in another.

## Where it slipped

Most of the mistakes came from one part of the Second Republic chapter, which tells the history of Spain's flag and coat of arms from the 1800s. One card says the Second Republic's flag carried the motto "Constitución", when the text is talking about a flag from the 1820s. Another says the Republic lasted until the Civil War began, when the chapter itself says it lasted until 1 April 1939.

Other cards got the main point but added something the text doesn't say, like calling a thread "strong" or saying Arkwright "started the textile industry". One translated a term badly (a cotton gin isn't a "spinning machine"), and a few repeated an earlier card in other words. In these tests the written study guide also stopped mid-sentence before the cards. The app team found the cause, and it's fixed for the next version.

So use the cards, but check them before you study, especially for chapters that mix dates from different periods. Checking 18 cards takes a couple of minutes, which is still far faster than writing them by hand.

## Other ways to make AI flashcards for free

All of these run online, so you upload your PDF to their site. The facts are from their own pages in October 2026; we haven't measured their quality.

| Tool | Free | Uploads your PDF? |
| --- | --- | --- |
| **NotebookLM** (Google) | Yes: flashcards and quizzes from your documents, exportable as CSV, citing the original text ([Google](https://support.google.com/notebooklm/answer/16958963?hl=en)) | Yes, to Google |
| **SlideSpeak** | Yes, PDFs up to 50 pages, no account, exports to Anki or Quizlet ([SlideSpeak](https://slidespeak.co/free-tools/create-flashcards-from-pdf)) | Yes |
| **Flashcards.world** | Up to 10 cards without signing up ([Flashcards.world](https://flashcards.world/pdf-to-flashcards/)) | Yes |
| **GreenCube** (on your PC) | €9.99 once, no limits; it also chats, summarizes and answers questions about the chapter | **No**: everything stays on your computer |

If you don't mind uploading your notes to Google, NotebookLM is a very complete free option. If you'd rather they never left your computer, don't want limits, or study without a good connection, you need an AI on your own PC. We checked what each AI does with your uploads in [Which AI doesn't train on your chats?](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data)

## How to get good flashcards from a PDF

- Do one chapter at a time. A chapter gives 18 fairly focused cards; a whole book dilutes them.
- Check the cards about dates from other periods, since that's where it slips most.
- Delete the repeats and the vague ones ("What is the shaping machine?" answered with "A machine used in the development of machine tools") and keep the ones that make you think.
- Ask for exam-style questions too, and answer them without looking. In [our PDF questions test](https://blog.greencube.app/blog/ai-to-study-from-pdf) it got 11 of 12 right, in about 15 seconds each.

Not sure it will run on your computer? [Check in 30 seconds](https://blog.greencube.app/blog/can-my-pc-run-ai#checker). With a graphics card it's much faster than on this laptop.

## FAQ

### Can I make AI flashcards from a PDF without internet?

Yes, with an AI on your computer. In our test GreenCube turned a 4,800-word chapter into 18 flashcards and a study guide in about 5 minutes, on a 16 GB laptop with no graphics card and no connection.

### Are AI-made flashcards reliable?

Mostly, so check them before you study. Of 36 cards we checked by hand, the small AI got 21 right, 6 partly right, 5 wrong and 4 repeats; the bigger one got 30 right, 4 partly, 2 wrong and no repeats. Most mistakes came from the part of the chapter that jumps between periods.

### Can it make flashcards in another language than the PDF?

Yes. We asked for Spanish flashcards from an English chapter and all 18 came out in Spanish: 11 right, 4 partly right, none wrong and 3 repeats.

### What's the best free app to make AI flashcards from a PDF?

NotebookLM, if you don't mind uploading the PDF: it's free, exports flashcards as CSV and cites the original text. If you don't want to upload it or hit limits, you need an AI on your own PC.
