# Rock Paper Scissors player using pattern history

def player(prev_play, opponent_history=[], my_history=[]):
    
    if not prev_play:
        opponent_history.clear()
        my_history.clear()
        return 'R'
    
    opponent_history.append(prev_play)
    
    ideal = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = 'R'
    
    # Try to find patterns - use longer patterns for better prediction
    best_prediction = None
    max_count = 0
    
    for pattern_len in range(min(15, len(opponent_history)), 0, -1):
        # Get the recent pattern from opponent
        pattern = "".join(opponent_history[-pattern_len:])
        
        # Count what came after this pattern in history
        predictions = {'R': 0, 'P': 0, 'S': 0}
        
        # Build full opponent history string (excluding current move)
        history = "".join(opponent_history[:-1])
        
        # Search for this pattern in history
        for i in range(len(history) - pattern_len):
            if history[i:i+pattern_len] == pattern:
                # What did opponent play next?
                if i + pattern_len < len(opponent_history) - 1:
                    next_move = opponent_history[i + pattern_len]
                    predictions[next_move] += 1
        
        # Track the best prediction
        total = sum(predictions.values())
        if total > 0:
            predicted_move = max(predictions, key=lambda k: predictions[k])
            if predictions[predicted_move] > max_count:
                max_count = predictions[predicted_move]
                best_prediction = predicted_move
            
            # Use longer patterns if they have good confidence
            if total >= 2:  # At least 2 matches
                guess = ideal[predicted_move]
                my_history.append(guess)
                return guess
    
    # Use best prediction if we have one
    if best_prediction:
        guess = ideal[best_prediction]
    # Fallback to most common recent move
    elif len(opponent_history) > 2:
        recent = opponent_history[-30:]
        most_common = max(set(recent), key=recent.count)
        guess = ideal[most_common]
    
    my_history.append(guess)
    return guess
