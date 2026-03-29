tool_description = """
                Search for similar symptoms/recommendations in the medical cases database.

                How it works:
                1. Receives a user query describing symptoms or medical concerns.
                2. Converts the query into a semantic vector using the embedding client.
                3. Performs a similarity search in the Qdrant collection 'medical_cases'.
                4. Optionally filters results using `filter_payload`:
                   - `filter_payload` is a dictionary where each key corresponds to a field in the metadata.
                   - Each value should be a dictionary with one of the following:
                       * {"any": [values]} — matches if any value in the list is present in the field.
                       * {"match": value} — matches if the field exactly equals the value.
                   - Example:
                       filter_payload = {
                           "symptoms": {"any": ["fever", "sore throat"]},
                           "doctor": {"match": "general practitioner"}
                       }
                5. Returns top-k results, formatted as:
                   1. Case text
                      Metadata: {metadata dictionary}
                6. If no relevant cases are found, returns "No relevant medical cases found."""