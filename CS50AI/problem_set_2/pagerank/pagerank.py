import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_dict = {}
    links = corpus[page]
    if len(links) == 0:
        for webpage in corpus:
            prob_dict[webpage] = 1 / len(corpus)
        return prob_dict
    else:
        for webpage in corpus:
            if webpage in links:
                prob_dict[webpage] = damping_factor / len(links) + (1 - damping_factor) / len(corpus)
            else:
                prob_dict[webpage] = (1 - damping_factor) / len(corpus)
        return prob_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Iteration
    i = 0
    # Create the dictionary to keep track of the number of times each website appeared in sample
    pagerank_dict = {webpage: 0 for webpage in corpus}
    # Randomly draw the first page and update the data
    link_list = list(corpus.keys())
    link_choice = random.choice(link_list)
    pagerank_dict[link_choice] += 1
    i += 1

    # Update the corresponding webpage and iterations using loop to simulate the random web surfer
    while i < n:
        # Probability distribution for all the links in the current page
        prob_dist = []
        prob_for_current_page = transition_model(corpus, link_choice, damping_factor)
        for link in prob_for_current_page:
            prob_dist.append(prob_for_current_page[link])
        link_choice = random.choices(link_list, weights=prob_dist, k=1)[0]
        pagerank_dict[link_choice] += 1
        i += 1

    pagerank_prob = {page_name: page_rank/n for (page_name, page_rank) in pagerank_dict.items()}
    return pagerank_prob


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    threshold = 0.001
    pagerank_dict = {webpage: 1 / len(corpus) for webpage in corpus}
    diff = 1
    # Setting the pages with no links to link to all pages in the corpus
    for page in corpus:
        if len(corpus[page]) == 0:
            corpus[page] = list(corpus.keys())
    while diff > threshold:
        diff = 0
        update_dict = {}
        for page in pagerank_dict:
            new_prob = (1 - damping_factor) / len(corpus) + damping_factor * \
                sum(pagerank_dict[link] / len(corpus[link])
                    for link in corpus if page in corpus[link])
            if abs(pagerank_dict[page] - new_prob) > diff:
                diff = abs(pagerank_dict[page] - new_prob)
            update_dict[page] = new_prob
        pagerank_dict.update(update_dict)
    return pagerank_dict


if __name__ == "__main__":
    main()
