#include "Scene.h"

#include "Common.h"
#include "physics/MotionIntegrators.h"
#include "physics/Transform.h"

#include <string>

using namespace std::string_literals;

void Scene::init(int width, int height)
{
	resize(width, height);

	m_world.camera.setPosition({ 0.0f, 1.0f, 3.0f });
	m_world.camera.setPitch(-20.0f);

	//Monkey
	EntityObject* monkey = new EntityObject("./res/models/monkey.obj", { "./res/shaders/shader.vert", "./res/shaders/shader.frag" });
	monkey->getTransform().position(glm::vec3(0.0f, -1.5f, 0.0f));

	m_entities.push_back(monkey);

	//Plane
	EntityObject* plane = new EntityObject("./res/models/plane.obj", { "./res/shaders/shader.vert", "./res/shaders/shader.frag" });
	plane->getTransform().position(glm::vec3(0.0f, -2.5f, 0.0f));
	plane->getTransform().scale(glm::vec3(10.0f));

	m_entities.push_back(plane);
}

void Scene::update(double delta)
{
	m_world.camera.update(delta);

	for (Entity* entity : m_entities)
	{
		entity->update(delta);
	}
}

void Scene::render()
{
	glClearColor(1.0f, 0.0f, 0.0f, 1.0f);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	for (Entity* entity : m_entities)
	{
		entity->render(m_world);
	}
}

void Scene::resize(int width, int height)
{
	glViewport(0, 0, width, height);

	m_world.camera.resize(width, height);
}

void Scene::destroy()
{
	for (Entity* entity : m_entities)
	{
		delete entity;
	}
}

Scene* Scene::singleton()
{
	static Scene scene;
	return &scene;
}