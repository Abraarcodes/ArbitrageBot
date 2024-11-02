window.onload = function() {
    // Get the table element
    const table = document.getElementById('dashboardTable');

    // Fetch the data from the text file or your data source
    fetch('all_opportunities_profits.txt')
        .then(response => response.text())
        .then(data => {
            // Parse the data as a JavaScript array
            const dataArray = JSON.parse(data);

            // Calculate the sum of all values
            const sum = dataArray.reduce((acc, val) => acc + val, 0);

            // Add the initial investment row
            const initialInvestmentRow = table.insertRow();
            const initialInvestmentCell = initialInvestmentRow.insertCell();
            initialInvestmentCell.innerHTML = 'Initial Investment';
            const initialInvestmentValueCell = initialInvestmentRow.insertCell();
            initialInvestmentValueCell.innerHTML = '10000';

            // Add the sum of elements row
            const sumOfElementsRow = table.insertRow();
            const sumOfElementsCell = sumOfElementsRow.insertCell();
            sumOfElementsCell.innerHTML = 'Current investment';
            const sumOfElementsValueCell = sumOfElementsRow.insertCell();
            sumOfElementsValueCell.innerHTML = (sum + 10000).toFixed(4); // Limit decimal places as needed

            const returnsRow = table.insertRow();
            const returnsCell = returnsRow.insertCell();
            returnsCell.innerHTML = 'Returns';
            const returnsValueCell = returnsRow.insertCell();
            const initialInvestment = 10000;
            const currentInvestment = sum + initialInvestment;
            const returns = ((currentInvestment - initialInvestment) / initialInvestment) * 100;
            returnsValueCell.innerHTML = returns.toFixed(2) + '%';

        })
        .catch(error => console.error('Error fetching data:', error));
};
