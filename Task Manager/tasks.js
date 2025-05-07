console.log("Login script loaded");

document.addEventListener('DOMContentLoaded', function () {
    // DOM Elements
    let tasks = [];
    let currentCategory = 'all';
    let currentSortOrder = 'date-desc'; 
    const taskList = document.getElementById('task-list');
    const emptyState = document.getElementById('empty-state');
    const addTaskBtn = document.getElementById('add-task-btn');
    const taskModal = document.getElementById('task-modal');
    const closeModalBtn = document.getElementById('close-modal');
    const cancelBtn = document.getElementById('cancel-btn');
    const taskForm = document.getElementById('task-form');
    const modalTitle = document.getElementById('modal-title');
    const taskIdInput = document.getElementById('task-id');
    const taskTitleInput = document.getElementById('task-title-input');
    const taskDescriptionInput = document.getElementById('task-description');
    const taskDueDateInput = document.getElementById('task-due-date');
    const taskPriorityInput = document.getElementById('task-priority');
    const searchInput = document.getElementById('search-input');
    const categoryItems = document.querySelectorAll('.category-item');
    const totalTasksEl = document.getElementById('total-tasks');
    const completedTasksEl = document.getElementById('completed-tasks');
    const pendingTasksEl = document.getElementById('pending-tasks');
    const sortBtn = document.getElementById('sort-btn');
    const loginForm = document.getElementById('login-form');
    console.log("loginForm:", loginForm);
    const registerForm = document.getElementById('register-form');
    const authContainer = document.querySelector('.auth-container'); // Get the auth container
    const dashboardContainer = document.querySelector('.dashboard-container'); // Get the dashboard container
    const baseUrl = "http://localhost:5161"; // Change to your backend URL if different
    const authUrl = `${baseUrl}/api/auth`;
    const apiUrl = `${baseUrl}/api/tasks`;

        // Handle navigation links
        const registerLink = document.getElementById("show-register");
        const forgotPasswordLink = document.getElementById("forgot-password");

        if (registerLink) {
            registerLink.addEventListener("click", (e) => {
                e.preventDefault(); // prevent default anchor behavior
                window.location.href = "register.html"; // redirect to register page
            });
        }

        if (forgotPasswordLink) {
            forgotPasswordLink.addEventListener("click", (e) => {
                e.preventDefault();
                window.location.href = "forgot-password.html"; // redirect to forgot password page
            });
        }

        // Login form event listener
        if (loginForm) {
            loginForm.addEventListener('submit', function (e) {
                e.preventDefault(); // Prevent default form submission
                
                // Only use the e.target.querySelector() to get the values
                const email = e.target.querySelector('#login-email').value;
                const password = e.target.querySelector('#login-password').value;
        
                console.log("Login form submitted for:", email);
                
                // Call the loginUser function with the form data
                loginUser({ email, password });
            });
        }

// Handle user login
async function handleLogin(event) {
    event.preventDefault(); // Prevent form from reloading the page

    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    const loginRequest = {
        UserEmail: email,
        UserPassword: password
    };

    try {
        const response = await fetch('http://localhost:5161/api/users/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'include', // ✅ Required for cookie-based auth
            body: JSON.stringify(loginRequest)
        });

        if (response.ok) {
            const data = await response.json();
            console.log('✅ Login successful:', data);
            alert("Login successful!");

            // Redirect to dashboard after successful login
            window.location.href = "dashboard.html";  // Ensure this is uncommented
        } else {
            // Handle different status codes and provide useful error messages
            let errorMessage = 'Login failed. Please check your credentials.';
            if (response.status === 401) {
                errorMessage = 'Invalid email or password. Please try again.';
            } else if (response.status === 500) {
                errorMessage = 'Server error. Please try again later.';
            }
            console.warn('❌ Login failed:', errorMessage);
            alert(errorMessage);
        }
    } catch (error) {
        console.error('⚠️ Network or server error during login:', error);
        alert("An error occurred while logging in. Please try again.");
    }
} 
  
        // Register form event listener
if (registerForm) {
    registerForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent default form submission
        
        // Use querySelector to get values from the form inputs
        const username = e.target.querySelector('#register-username').value;
        const email = e.target.querySelector('#register-email').value;
        const password = e.target.querySelector('#register-password').value;
        
        console.log("Registration form submitted for:", email);
        
        // Call the registerUser function with the form data
        registerUser({ username, email, password });
    });
}


        // Helper function to show notifications
        function showNotification(message, type = 'info') {
            const notificationContainer = document.getElementById('notification-container');
            if (!notificationContainer) return;

            const notification = document.createElement('div');
            notification.className = `notification ${type}`;
            notification.textContent = message;

            notificationContainer.appendChild(notification);

            // Remove notification after 5 seconds
            setTimeout(() => {
                notification.classList.add('fade-out');
                setTimeout(() => {
                    notificationContainer.removeChild(notification);
                }, 500);
            }, 5000);
        }

        function loginUser(credentials) {
            console.log('Attempting login...');
        
            // Validate credentials before sending request
            if (!credentials || !credentials.email || !credentials.password) {
                console.error('Missing email or password');
                showNotification?.('Please enter both email and password.', 'error');
                return;
            }
        
            // Check that authUrl is defined
            if (typeof authUrl === 'undefined') {
                console.error('authUrl is not defined.');
                showNotification?.('Server configuration error. Please try again later.', 'error');
                return;
            }
        
            const debugMode = false; // Set to true for local testing
            if (debugMode) {
                console.log('Debug mode: Simulating successful login');
                localStorage.setItem('authToken', 'debug-token-12345');
                window.location.href = "Dashboard.html";
                return;
            }
        
            // Adjust field names to match backend (UserEmail, UserPassword)
            const loginRequest = {
                UserEmail: credentials.email,
                UserPassword: credentials.password
            };
            
            fetch(`${authUrl}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(loginRequest),
            })
            .then(async response => {
                console.log('Login response status:', response.status);
        
                // Try to parse error details
                const data = await response.json().catch(() => ({}));
        
                if (!response.ok) {
                    const errorMessage = data.message || `Login failed with status: ${response.status}`;
                    throw new Error(errorMessage);
                }
        
                return data;
            })
            .then(data => {
                console.log('Login response received:', data);
        
                // If backend returns a success message, proceed to redirect
                if (data.message === "Login successful") {
                    console.log('Login successful, redirecting to dashboard');
                    window.location.href = "Dashboard.html"; // Redirect to dashboard after login
                } else {
                    console.error('Unexpected response:', data);
                    showNotification?.('Login failed. Please try again.', 'error');
                }
            })
            .catch(error => {
                console.error('Login Error:', error.message);
                showNotification?.(error.message || 'Error connecting to server. Please try again later.', 'error');
            });
        }
        

// Improved register function
function registerUser(credentials) {
    console.log('Attempting registration...');

    fetch(`${authUrl}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
    })
        .then(response => {
            console.log('Register response status:', response.status);
            if (!response.ok) {
                throw new Error(`Registration failed with status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Registration response received:', data);
            if (data.token) {
                localStorage.setItem('authToken', data.token);
                console.log('Auth token saved, redirecting to dashboard');
                window.location.href = "Dashboard.html"; // Consistent path with login
            } else {
                console.error('No token in response');
                showNotification('Registration failed. Please try again.', 'error');
            }
        })
        .catch(error => {
            console.error('Registration Error:', error);
            showNotification('Error connecting to server. Please try again later.', 'error');
        });
}

// Registration form submission logic with password confirmation
document.getElementById("register-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("register-username").value; // Changed to correct ID
    const email = document.getElementById("register-email").value;
    const password = document.getElementById("register-password").value;
    const confirmPassword = document.getElementById("register-confirm-password").value;

    // Check if passwords match
    if (password !== confirmPassword) {
        showNotification('Passwords do not match. Please try again.', 'error');
        return;
    }

    const credentials = {
        name: username, // Mapping the input ID correctly here
        userName: username, // Ensure the backend expects the same property
        userEmail: email,
        userPassword: password
    };

    registerUser(credentials);
});

// Check if user is already logged in
const checkAuthStatus = () => {
    const token = localStorage.getItem('authToken');
    if (token && window.location.pathname.includes('login.html')) {
        // If we're on the login page and have a token, redirect to dashboard
        window.location.href = "Dashboard.html";
    }
};

// Check auth status on page load
checkAuthStatus();

    function fetchTasks() {
        const token = localStorage.getItem('authToken');
        if (!token) return;

        fetch(apiUrl, {
            headers: { 'Authorization': `Bearer ${token}` }
        })
            .then(response => response.json())
            .then(data => {
                tasks = data;
                renderTasks();
                updateStats();
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
                alert('Failed to load tasks.');
            });
    }

    function renderTasks() {
        const searchQuery = searchInput.value.toLowerCase();
        let filteredTasks = tasks;

        if (currentCategory !== 'all') {
            filteredTasks = filteredTasks.filter(task => {
                if (currentCategory === 'today') {
                    const today = new Date();
                    today.setHours(0, 0, 0, 0);
                    const dueDate = new Date(task.dueDate);
                    dueDate.setHours(0, 0, 0, 0);
                    return dueDate.getTime() === today.getTime();
                } else if (currentCategory === 'important') {
                    return task.priority === 'high';
                } else if (currentCategory === 'completed') {
                    return task.completed;
                }
                return true;
            });
        }

        if (searchQuery) {
            filteredTasks = filteredTasks.filter(task =>
                task.title.toLowerCase().includes(searchQuery) ||
                (task.description && task.description.toLowerCase().includes(searchQuery))
            );
        }

        sortTasks(filteredTasks);

        const fragment = document.createDocumentFragment();
        filteredTasks.forEach(task => {
            const taskItem = document.createElement('li');
            taskItem.className = `task-item ${task.completed ? 'completed' : ''} ${task.priority === 'high' ? 'important' : ''}`;
            taskItem.innerHTML = `
                <div class="task-info">
                    <div class="task-title">${task.title}</div>
                    <div class="task-meta">
                        <span class="task-date">${task.dueDate ? new Date(task.dueDate).toLocaleDateString() : 'No due date'}</span>
                        <span class="task-priority">${task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}</span>
                    </div>
                </div>
                <div class="task-actions">
                    <button class="task-btn toggle-completed" data-id="${task.id}"><i class="material-icons">${task.completed ? 'check_circle' : 'radio_button_unchecked'}</i></button>
                    <button class="task-btn edit-task" data-id="${task.id}"><i class="material-icons">edit</i></button>
                    <button class="task-btn delete-task" data-id="${task.id}"><i class="material-icons">delete</i></button>
                </div>
            `;
            fragment.appendChild(taskItem);
        });

        taskList.innerHTML = '';
        taskList.appendChild(fragment);

        document.querySelectorAll('.toggle-completed').forEach(btn => {
            btn.addEventListener('click', toggleTaskCompleted);
        });

        document.querySelectorAll('.edit-task').forEach(btn => {
            btn.addEventListener('click', editTask);
        });

        document.querySelectorAll('.delete-task').forEach(btn => {
            btn.addEventListener('click', deleteTask);
        });

        if (filteredTasks.length === 0) {
            emptyState.style.display = 'block';
        } else {
            emptyState.style.display = 'none';
        }
    }

    function sortTasks(taskArray) {
        if (currentSortOrder === 'date-desc') {
            taskArray.sort((a, b) => new Date(b.dueDate) - new Date(a.dueDate));
        } else if (currentSortOrder === 'date-asc') {
            taskArray.sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate));
        } else if (currentSortOrder === 'priority') {
            taskArray.sort((a, b) => a.priority.localeCompare(b.priority));
        }
    }

    function updateStats() {
        totalTasksEl.textContent = tasks.length;
        const completedCount = tasks.filter(task => task.completed).length;
        completedTasksEl.textContent = completedCount;
        pendingTasksEl.textContent = tasks.length - completedCount;
    }

    // --- Password Visibility Toggle ---
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    
    togglePasswordButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get the parent password-field div
            const passwordField = this.closest('.password-field');
            
            // Find the password input within the same password-field div
            const passwordInput = passwordField.querySelector('input');
            
            // Get the eye icon
            const eyeIcon = this.querySelector('i');
    
            // Toggle password visibility
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                eyeIcon.classList.remove('fa-eye');
                eyeIcon.classList.add('fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                eyeIcon.classList.remove('fa-eye-slash');
                eyeIcon.classList.add('fa-eye');
            }
        });
    });
    
    function init() {
        fetchTasks(); // Maybe other setup too
    }
})
