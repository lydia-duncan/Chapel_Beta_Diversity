import chapelBetaDiversity.betaDiversity

betaDiversity.chpl_setup()

result = betaDiversity.beta_diversity(in_name="Utila", map_type="geomorphic",
                                      window_size=12732)

print(result)

betaDiversity.chpl_cleanup()
