# Brief for the French translation

All paths are relative to `kanuni-i-leke-dukagjinit/`.

## Sources

- **Translate from the Albanian**, `sq/kanuni.md`: Gheg, 1933 spelling, often corrupt.
- Use the English, `en/kanuni.md`, to check your reading. It is a careful but unverified draft. Where you are sure the English misreads the Albanian, follow the Albanian and write it down in your notes file.
- `working/notes.md` has, book by book, the corrupt passages, the uncertain readings and the words still unidentified. Read the section for your books before you start.
- `fr/glossary.md` holds the **mandatory** French renderings of the customary terms. Use them every time. If a term is missing, choose a rendering, keep it consistent, and write it in your notes.

The two source files line up line by line: line N of `sq/kanuni.md` is line N of `en/kanuni.md`. Your part must have **exactly the same lines**, in the same order:
- one French line for each source line;
- blank lines where the source has blank lines.

## Markdown format (do not change the structure)

- **Headings** keep their level and their `{#id}` exactly. Numbers become Roman numerals matching the id. Book titles stay in capitals, as in the source.
  - `## LIVRE I — L'ÉGLISE {#book-1}`
  - `### Article premier — PARTIE CIVILE {#article-1}` and `### Article deuxième — PARTIE PÉNALE {#article-2}`
  - `### CHAPITRE XXIV — La mort. {#chapter-24}`
  - `#### SECTION LXVI. {#section-66}`: a section with no title keeps no title.
- **Paragraphs** start with `**§ 601.**` exactly: bold, a space, the number, a full stop.
- **Numbered items** are written `1\.` or `10\)`, with the backslash, as in the source. Lettered items are `a)`. Keep the same numbering or lettering as the source line.
- **Gjeçovi's notes**:
  - the lines `<div class="note" markdown="1">` and `</div>` stay unchanged;
  - the label *Oroe* / *V.O.* / "Note" becomes `Note :` (or `Note.` if the source has a full stop and nothing after it).
- **Editorial notes** `> *[…]*` are translated; keep the `> *[` … `]*` markup.
- **Square brackets** in the text mark editorial additions or corrupt passages. Keep the ones that are needed, translated into French. Do not add commentary inside the text beyond what the English already has, unless the Albanian requires it.
- **Quotation marks:** use straight double quotes `"…"` only, never « » or “ ”; the build turns them into « » with non-breaking spaces. Use a straight apostrophe `'`.
- **French spacing:** put an ordinary space before `:` `;` `!` `?`. The build will make it non-breaking.
- **Italics:** the Albanian terms kept in the text (*besa*, *shengjeta*, *sedija*, *Nun*, *krushq*…) are in `*italics*`, as in the English.

## Style

- Literal, sober, legal French, close to the Albanian. It should read like a customary code, not a paraphrase. Keep the short sentences short.
- Proverbs and maxims (the lines in quotation marks) are translated literally and concisely; it is fine if they sound archaic.
- Use the future of obligation for "do të…" ("il paiera", "il devra"), the present for the general rule.
- *mik* is always "l'hôte" (the guest). The one who receives is "le maître de maison". Never use "hôte" for the person receiving.
- Do not consult or reproduce any published French or English translation (Christian Gut, Leonard Fox): this translation is made from the public-domain Albanian.

## What to produce

1. `fr/parts/NN.md`: your translation of the line range you were given.
2. `fr/parts/NN.notes.md`: your translation notes, in English, short bullets:
   - uncertain readings, with the § number;
   - places where you depart from the English, and why;
   - terms missing from the glossary, with the rendering you chose.
3. Check the structure: `python3 -I working/fr_check.py fr/parts/NN.md FIRST LAST`. It must print `OK`.
