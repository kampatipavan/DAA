# E-Commerce Recommendation System
# Graph-Based Ranking using Jaccard Similarity

# ---------------------------------------------------
# User-Product Interaction Data
# ---------------------------------------------------

user_products = {
    "User1": {"Laptop", "Mouse", "Keyboard"},
    "User2": {"Laptop", "Mouse", "Headphones"},
    "User3": {"Laptop", "Keyboard", "Laptop Bag"},
    "User4": {"Phone", "Earphones", "Power Bank"},
    "User5": {"Laptop", "Mouse", "Laptop Bag"}
}


# ---------------------------------------------------
# Jaccard Similarity
# ---------------------------------------------------

def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    if union == 0:
        return 0

    return intersection / union


# ---------------------------------------------------
# Find Similar Users
# ---------------------------------------------------

def find_similar_users(target_user):
    similarities = {}

    for user in user_products:

        if user != target_user:

            similarity = jaccard_similarity(
                user_products[target_user],
                user_products[user]
            )

            similarities[user] = similarity

    return similarities


# ---------------------------------------------------
# Generate Recommendations
# ---------------------------------------------------

def recommend_products(target_user, top_n=3):

    target_products = user_products[target_user]

    # Find similarity with other users
    similarities = find_similar_users(target_user)

    recommendations = {}

    for user, similarity in similarities.items():

        # Consider products of similar users
        for product in user_products[user]:

            # Do not recommend products already used
            if product not in target_products:

                if product not in recommendations:
                    recommendations[product] = 0

                # Ranking score
                recommendations[product] += similarity

    # Sort products according to ranking score
    ranked_products = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_products[:top_n]


# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

target_user = "User1"

print("E-COMMERCE RECOMMENDATION SYSTEM")
print("--------------------------------")

print("\nProducts used by", target_user, ":")
print(user_products[target_user])

print("\nUser Similarities:")

similarities = find_similar_users(target_user)

for user, score in similarities.items():
    print(user, "->", round(score, 2))

print("\nRecommended Products:")

recommendations = recommend_products(target_user)

for product, score in recommendations:
    print(product, "-> Ranking Score:", round(score, 2))
