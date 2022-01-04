# %% [markdown]
# # 10. Hashing and Hash

# %%
# hash for integer unchanged
print("Hash for 100 is:", hash(100))
# hash for decimal
print("Hash for 100.55 is:", hash(100.55))
# hash for string
print("Hash for CFG is:", hash("CFG"))
# hash for tuple
word = ("g", "i", "r", "l", "s")
print("The hash is:", hash(word))

# %%
from pprint import pp


class CFGStudent:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other: object) -> bool:
        return self.age == other.age and self.name == other.name

    def __hash__(self) -> int:
        tuple = (self.age, self.name)
        return hash(tuple)

    def __repr__(self):
        return self.name


# %%
nina = CFGStudent(30, "Nina")
roshni = CFGStudent(30, "Roshni")
roshni_b = CFGStudent(30, "Roshni")

print(f"The hash is {hash(nina)}")
print(f"The hash is {hash(roshni)}")
print(f"The hash is {hash(roshni_b)}")

dict = {nina: "red", roshni: "blue", roshni_b: "green"}

pp(dict)

# %% [markdown]
# #### Open Me

# %% [markdown]
# ```
# If a == b then hash(a) == hash(b)
# If hash(a) == hash(b), then a might equal b
# If hash(a) != hash(b), then a != b
# ```

# %% [markdown]
# When inserting an item:
# 1. Call `__hash__` to compute the hash of the key.
# 2. Store the hash, key and value in an array to location `hash % len(list)`
#
# When retrieving an item:
# 1. Call `__hash__` to compute the hash o the key.
# 2. Look in `hash % len(list`) for entry that matches the hash. If found, check for equality by identity, then by calling `__eq__`
