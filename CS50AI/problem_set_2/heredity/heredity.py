import csv
import itertools
import sys
import numpy

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    def parent_probability(genes, passed_gene):
        if genes == 0:
            if passed_gene:
                return PROBS["mutation"]
            else:
                return 1 - PROBS["mutation"]
        elif genes == 1:
            return 0.5 * PROBS["mutation"] + 0.5 * (1 - PROBS["mutation"])
        elif genes == 2:
            if passed_gene:
                return 1 - PROBS["mutation"]
            else:
                return PROBS["mutation"]

    # Add the gene number and trait to the people dictionary
    for person in people:
        people[person]["trait"] = person in have_trait
        if person in one_gene:
            people[person]["gene"] = 1
        elif person in two_genes:
            people[person]["gene"] = 2
        else:
            people[person]["gene"] = 0

    probability_list= []
    for person in people:
        # If person does not have parents
        if not people[person]["mother"] or not people[person]["father"]:
            # One gene
            if people[person]["gene"] == 1:
                probability = PROBS["gene"][1]
                # With trait
                if person in have_trait:
                    probability *= PROBS["trait"][1][True]
                # No traits
                else:
                    probability *= PROBS["trait"][1][False]
                probability_list.append(probability)
            # Two genes
            elif people[person]["gene"] == 2:
                probability = PROBS["gene"][2]
                if person in have_trait:
                    probability *= PROBS["trait"][2][True]
                else:
                    probability *= PROBS["trait"][2][False]
                probability_list.append(probability)
            # No genes
            else:
                probability = PROBS["gene"][0]
                if person in have_trait:
                    probability *= PROBS["trait"][0][True]
                else:
                    probability *= PROBS["trait"][0][False]
                probability_list.append(probability)
        # If person has parents
        else:
            # Child with one gene(one from dad, none from mum / none from dad, one from mum)
            if person in one_gene:
                # One from dad, none from mum
                case1 = parent_probability(people[people[person]["father"]]["gene"], True) * parent_probability(people[people[person]["mother"]]["gene"], False)
                # None from dad, one from mum
                case2 = parent_probability(people[people[person]["father"]]["gene"], False) * parent_probability(people[people[person]["mother"]]["gene"], True)
                prob = case1 + case2
            # Child with two genes(one from dad, one from mum)
            elif person in two_genes:
                prob = parent_probability(people[people[person]["father"]]["gene"], True) * parent_probability(people[people[person]["mother"]]["gene"], True)
            # Child with no genes(none from dad, none from mum)
            else:
                prob = parent_probability(people[people[person]["father"]]["gene"], False) * parent_probability(people[people[person]["mother"]]["gene"], False)
            # Multiply the gene probability with trait probability
            final_prob = prob * PROBS["trait"][people[person]["gene"]][people[person]["trait"]]
            probability_list.append(final_prob)
    return numpy.prod(probability_list)


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """

    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
            if person in have_trait:
                probabilities[person]["trait"][True] += p
            else:
                probabilities[person]["trait"][False] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
            if person in have_trait:
                probabilities[person]["trait"][True] += p
            else:
                probabilities[person]["trait"][False] += p
        else:
            probabilities[person]["gene"][0] += p
            if person in have_trait:
                probabilities[person]["trait"][True] += p
            else:
                probabilities[person]["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        total_gene_prob = sum(probabilities[person]["gene"].values())
        for gene_number in probabilities[person]["gene"]:
            probabilities[person]["gene"][gene_number] /= total_gene_prob
        total_trait_prob = sum(probabilities[person]["trait"].values())
        for trait_value in probabilities[person]["trait"]:
            probabilities[person]["trait"][trait_value] /= total_trait_prob


if __name__ == "__main__":
    main()
