document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('fitFusionForm');
    const allergiesSelect = document.getElementById('allergies');
    const allergyDetailsInput = document.getElementById('allergyDetails');
    const allergyLabel = document.getElementById('allergyLabel');
    const goalsSelect = document.getElementById('goals');
    const goalDetailsInput = document.getElementById('goalDetails');
    const goalLabel = document.getElementById('goalLabel');
    const resultDiv = document.getElementById('result');

    // Toggle allergy details input visibility
    allergiesSelect.addEventListener('change', () => {
        const showAllergyDetails = allergiesSelect.value === 'yes';
        allergyDetailsInput.style.display = showAllergyDetails ? 'block' : 'none';
        allergyLabel.style.display = showAllergyDetails ? 'block' : 'none';
    });

    // Toggle goal details input visibility
    goalsSelect.addEventListener('change', () => {
        const showGoalDetails = goalsSelect.value === 'yes';
        goalDetailsInput.style.display = showGoalDetails ? 'block' : 'none';
        goalLabel.style.display = showGoalDetails ? 'block' : 'none';
    });

    // Handle form submission
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const age = parseInt(document.getElementById('age').value);
        const height = parseInt(document.getElementById('height').value);
        const weight = parseInt(document.getElementById('weight').value);
        const BMI = weight / ((height / 100) ** 2);
        const allergies = document.getElementById('allergies').value === 'yes';
        const allergyDetails = allergyDetailsInput.value.trim();
        const goals = document.getElementById('goals').value === 'yes';
        const goalDetails = goalDetailsInput.value.trim();

        let resultHTML = `<h2>Results</h2>`;
        resultHTML += `<p>Your BMI is ${BMI.toFixed(2)}.</p>`;

        if (goals) {
            resultHTML += `<p>Your fitness goals: ${goalDetails}</p>`;
        } else {
            const suggestedWeightGoal = (22 * (height / 100) ** 2).toFixed(2);
            if (BMI < 18.5) {
                resultHTML += `<p>You are underweight. Your suggested weight goal is ${suggestedWeightGoal} kg.</p>`;
            } else if (BMI > 25) {
                resultHTML += `<p>You are overweight. Your suggested weight goal is ${suggestedWeightGoal} kg.</p>`;
            } else {
                resultHTML += `<p>You are at a healthy weight.</p>`;
            }
        }

        resultHTML += `<h3>Diet Plan</h3>`;
        if (age < 18) {
            resultHTML += `
                <p>Your diet plan (for under 18):</p>
                <ul>
                    <li>Breakfast: Whole Grain Cereal with Milk: A bowl of whole-grain cereal with milk and a piece of fruit.</li>
                    <li>Breakfast: Smoothie: Blend milk or a milk alternative with a banana, berries, and spinach.</li>
                    <li>Lunch: Grilled Chicken Sandwich: Whole-grain bread with grilled chicken, lettuce, and tomato.</li>
                    <li>Lunch: Veggie Sticks: Carrot and cucumber sticks with hummus.</li>
                    <li>Dinner: Spaghetti with Meat Sauce: Whole-grain spaghetti with a homemade meat sauce and a side of steamed broccoli.</li>
                    <li>Snacks: Yogurt with Fruit: A serving of yogurt with fresh fruit.</li>
                    <li>Snacks: Whole Grain Crackers with Cheese: A few whole-grain crackers with slices of cheese.</li>
                </ul>`;
        } else if (allergies) {
            resultHTML += `
                <p>Your diet plan (for those with allergies):</p>
                <ul>
                    <li>Breakfast: Gluten-Free Oatmeal: Cook 1 cup of gluten-free oats with a milk alternative. Add fruit and nuts.</li>
                    <li>Lunch: Quinoa Salad: Mix cooked quinoa with vegetables like bell peppers, cucumbers, and cherry tomatoes. Dress with olive oil and lemon.</li>
                    <li>Dinner: Baked Chicken with Sweet Potatoes: Baked chicken breast with roasted sweet potatoes and a side of green beans.</li>
                    <li>Snacks: Fruit Smoothie: Blend a milk alternative with fruits like bananas, berries, and a spoonful of nut butter.</li>
                    <li>Snacks: Vegetable Sticks: Carrot, cucumber, and bell pepper sticks with hummus.</li>
                </ul>`;
        } else if (BMI < 18.5) {
            resultHTML += `
                <p>Your diet plan (for underweight):</p>
                <ul>
                    <li>Breakfast: Oatmeal with Nuts and Fruit: Cook 1 cup of oats with milk or a milk alternative. Top with a handful of almonds or walnuts and fresh fruit.</li>
                    <li>Lunch: Chicken or Turkey Wrap: Whole-grain tortilla with grilled chicken or turkey, mixed greens, and avocado.</li>
                    <li>Dinner: Salmon or Chicken Breast: Baked or grilled salmon or chicken breast with sweet potato and steamed vegetables.</li>
                    <li>Snacks: Greek Yogurt with Honey and Granola: Greek yogurt topped with honey and granola.</li>
                    <li>Snacks: Trail Mix: A small handful of mixed nuts, dried fruit, and dark chocolate chips.</li>
                </ul>`;
        } else if (18.5 <= BMI <= 24.9) {
            resultHTML += `
                <p>Your diet plan (for healthy weight):</p>
                <ul>
                    <li>Breakfast: Whole-Grain Toast with Avocado: Whole-grain toast topped with mashed avocado and a poached egg.</li>
                    <li>Lunch: Grilled Chicken Salad: Mixed greens with grilled chicken, cherry tomatoes, cucumber, and a light vinaigrette.</li>
                    <li>Dinner: Baked Fish with Quinoa: Baked fish fillet with a side of quinoa and steamed broccoli.</li>
                    <li>Snacks: Fruit and Nut Butter: Apple slices with almond or peanut butter.</li>
                    <li>Snacks: Vegetable Sticks: Carrot and celery sticks with hummus.</li>
                </ul>`;
        } else {
            resultHTML += `
                <p>Your diet plan (for overweight):</p>
                <ul>
                    <li>Breakfast: Green Smoothie: Blend spinach, kale, green apple, banana, and a milk alternative.</li>
                    <li>Lunch: Vegetable Soup: A bowl of vegetable soup with a side of whole-grain bread.</li>
                    <li>Dinner: Grilled Chicken with Vegetables: Grilled chicken breast with a side of steamed vegetables and a small portion of brown rice.</li>
                    <li>Snacks: Greek Yogurt with Berries: Greek yogurt topped with fresh berries.</li>
                    <li>Snacks: Mixed Nuts: A small handful of mixed nuts.</li>
                </ul>`;
        }

        resultHTML += `<h3>Workout Plan</h3>`;
        if (age < 18) {
            resultHTML += `
                <p>Your workout plan (for under 18):</p>
                <ul>
                    <li>Cardiovascular Exercise: 30 minutes of running, cycling, or swimming, 3-5 times a week.</li>
                    <li>Strength Training: Bodyweight exercises like push-ups, squats, and planks, 2-3 times a week.</li>
                    <li>Flexibility: Stretching exercises or yoga, 2-3 times a week.</li>
                </ul>`;
        } else if (BMI < 18.5) {
            resultHTML += `
                <p>Your workout plan (for underweight):</p>
                <ul>
                    <li>Strength Training: Focus on weightlifting exercises such as squats, deadlifts, bench presses, and rows, 3-4 times a week.</li>
                    <li>Cardiovascular Exercise: Light cardio like walking or swimming, 2-3 times a week.</li>
                    <li>Flexibility: Stretching exercises or yoga, 2-3 times a week.</li>
                </ul>`;
        } else if (18.5 <= BMI <= 24.9) {
            resultHTML += `
                <p>Your workout plan (for healthy weight):</p>
                <ul>
                    <li>Cardiovascular Exercise: 30 minutes of moderate to intense cardio, such as running, cycling, or swimming, 3-5 times a week.</li>
                    <li>Strength Training: A mix of weightlifting and bodyweight exercises, 2-3 times a week.</li>
                    <li>Flexibility: Stretching exercises or yoga, 2-3 times a week.</li>
                </ul>`;
        } else {
            resultHTML += `
                <p>Your workout plan (for overweight):</p>
                <ul>
                    <li>Cardiovascular Exercise: 45 minutes of low-impact cardio, such as brisk walking, cycling, or swimming, 5 times a week.</li>
                    <li>Strength Training: Light to moderate weightlifting exercises, 2-3 times a week.</li>
                    <li>Flexibility: Stretching exercises or yoga, 3-4 times a week.</li>
                </ul>`;
        }

        resultDiv.innerHTML = resultHTML;
    });
});
