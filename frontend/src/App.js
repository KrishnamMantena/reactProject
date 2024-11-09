import React, { useState } from 'react';

function App() {
    const [projects, setProjects] = useState([]);
    const [projectDetails, setProjectDetails] = useState({ name: '', type: '', owner: '' });
    const [metric, setMetric] = useState({ name: '', value: '' });

    const addProject = () => {
        setProjects([...projects, projectDetails]);
        setProjectDetails({ name: '', type: '', owner: '' });
    };

    const addMetric = () => {
        console.log(`Metric added: ${metric.name} - ${metric.value}`);
        setMetric({ name: '', value: '' });
    };

    return (
        <div className="container">
            <h2>Add Project</h2>
            <input
                type="text"
                placeholder="Project Name"
                value={projectDetails.name}
                onChange={(e) => setProjectDetails({ ...projectDetails, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="Project Type"
                value={projectDetails.type}
                onChange={(e) => setProjectDetails({ ...projectDetails, type: e.target.value })}
            />
            <input
                type="text"
                placeholder="Project Owner"
                value={projectDetails.owner}
                onChange={(e) => setProjectDetails({ ...projectDetails, owner: e.target.value })}
            />
            <button onClick={addProject}>Add Project</button>

            <h2>Add Metrics</h2>
            <input
                type="text"
                placeholder="Metric Name"
                value={metric.name}
                onChange={(e) => setMetric({ ...metric, name: e.target.value })}
            />
            <input
                type="number"
                placeholder="Metric Value"
                value={metric.value}
                onChange={(e) => setMetric({ ...metric, value: e.target.value })}
            />
            <button onClick={addMetric}>Add Metric</button>

            <h2>Projects List</h2>
            <ul>
                {projects.map((project, index) => (
                    <li key={index}>
                        {project.name} - {project.type} - {project.owner}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
