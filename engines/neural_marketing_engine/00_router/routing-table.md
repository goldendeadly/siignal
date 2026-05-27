# Routing Table – Neural Marketing Engine v1

| Task Type                                   | Start Context          | Required Inputs                                     | Primary Outputs                                   |
|---------------------------------------------|------------------------|-----------------------------------------------------|----------------------------------------------------|
| **Create a new run**                        | `input-intake`         | niche, offer, avatar, tone, outcome, SEO intent     | run brief                                          |
| **Model strategy**                          | `strategy-modeling`    | run brief, avatar inputs, offer inputs              | strategy model                                     |
| **Generate blog titles**                    | `blog-generation`      | strategy model                                      | title set                                          |
| **Generate blog post**                      | `blog-generation`      | strategy model, selected title                      | long‑form blog                                     |
| **Generate social assets**                  | `signal-expansion`     | strategy model, blog post                           | multi‑platform social signal                       |
| **Generate ads**                            | `conversion-assets`    | strategy model, blog post or offer model            | ad copy set                                        |
| **Generate landing page**                   | `conversion-assets`    | strategy model, offer model                         | landing page draft                                 |
| **Refine outputs with performance feedback**| `optimization-recursion`| prior outputs, feedback data                        | revised outputs                                    |
| **Assemble delivery package**               | `packaging-output`     | all completed outputs                               | final delivery bundle                              |

This table is a quick reference for choosing the correct context based on the task at hand.  Always consult the router instructions before beginning work.