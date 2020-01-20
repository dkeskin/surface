#include "Scene.h"

#include "Common.h"
#include "physics/MotionIntegrators.h"
#include "physics/Transform.h"

#include "physics/entities/EntityGrid.h"
#include "physics/entities/EntityWater.h"

#include <string>

using namespace std::string_literals;

void Scene::init(int width, int height)
{
	resize(width, height);

	m_world.camera.setPosition({ 0.0f, 1.0f, 3.0f });
	m_world.camera.setPitch(-20.0f);

	EntityROV* rov = new EntityROV();
	rov->getTransform().position(glm::vec3(1.0f, 1.5f, -10.0f));
	rov->setThrusterPower(THRUSTER_BACK_RIGHT, 0.1f);
	rov->setThrusterPower(THRUSTER_BACK_LEFT, 0.1f);
	rov->setThrusterPower(THRUSTER_TOP_RIGHT, 0.1f);
	rov->setThrusterPower(THRUSTER_BOTTOM_LEFT, -0.1f);

	m_entities.push_back(rov);

	//m_entities.push_back(new EntityGrid(glm::vec2(30), glm::ivec2(10)));
	EntityWater* water = new EntityWater(38, 38, 70, 70);
	water->getTransform().position({ 0, 4, 0 });

	m_entities.push_back(water);

	MaterialData poolMaterial;
	poolMaterial.albedo = "./res/textures/texture.jpg";
	poolMaterial.vertexShader = "./res/shaders/shader.vert";
	poolMaterial.fragmentShader = "./res/shaders/shader.frag";
	poolMaterial.model = "./res/models/pool.obj";

	EntityObject* pool = new EntityObject(poolMaterial);
	m_entities.push_back(pool);
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
	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
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