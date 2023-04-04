# Hero story

story_1 = {
    "start": "Beginning of a Hero Story.",
    "middle": "Heroes actions and tasks.",
    "end": "Happy ending."
}

print(story_1)
print((type(story_1)))
print(story_1.keys())
print(story_1.values())

print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

story_1.update({
    "hero": "yourSuperHero"
})
print(story_1)
